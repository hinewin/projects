https://www.notion.so/Web-Scraping-With-Scrapy-and-MongoDB-102b8bfe85a580ceb58efbeff516e9a8?pvs=4
# Web Scraping With Scrapy and MongoDB

This project uses the `Scrapy` library to scrape information from a book website, then store it in MongoDB.

---

---

## Terminology

`Scrapy` - open-source Python framework for web scraping for extracting data from websites

`Spider` - Scrapy’s class that scape information from a website

`Element` - An individual component of an HTML web page

`Selector` - A pattern used to select one or more elements from a document

`item` - A container that defines the structure of the data that we want to collect (Python mapping/dictionary) 

---

# Setting up

## Install the Scrapy Package ([URL](https://realpython.com/web-scraping-with-scrapy-and-mongodb/#:~:text=performant%20web%20scraper.-,Install%20the%20Scrapy%20Package,-To%20get%20started))

```bash
(venv) $ python -m pip install scrapy
```

- Create a `scrapy` project

---

## Inspect the Source

- Inspect the site using browser’s `developer tool`
- Find the data points that we will need
    - Can gather `XPath` expressions or `CSS` selectors (this guide uses the later
- Example of selectors
    
    
    | Element | CSS Selector |
    | --- | --- |
    | Title | `#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a` |
    | Price | `#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > div.product_price > p.price_color` |
    | URL | `#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a` |
- Figure out the absolute paths, in this example it is within the `<article>` tag
    - Each element has a class name (`product_prod`)

---

## Preview Data with Scrapy Shell

- To test out the extracted data, use Scrapy CLI
- Open the shell and point to a site. This loads the URL and provides an interactive environment for the HTML’s structure
    
    ```bash
    (venv) $ scrapy shell http://books.toscrape.com
    ```
    
- The shell will provide some pre-imported projects (`response`) being the most important one to extract
    - `response.url` - URL of page
    - `response.status`- HTTP status code
    - `reponse.text`- Decoded text of the response as a Unicode string
- To test out the **CSS Selectors** from above, we need to set up a loop
    
    ```bash
    all_book_elements = response.css("article.product_pod")
    
    for book in all_book_elements:
        print(book.css("h3 > a::attr(title)").get())
    ```
    
    - Target all book container elements and store to `all_book_elements`
        - Calls to `.css()` return other `Selector` objects
    - Drill down further with another call to `.css()`
        - Need to define what value of the attribute, for example the `title` HTML attribute of all link elements within the `h3` element
        - `h3 > a::attr(title)`
        
        ```bash
        (book.css("h3 > a::attr(title)").get()
        ```
        
        - Calling `.get()` will return first match as a string

### Selector & Effect

Organize selectors to refine and ensure that we can extract the desired data when we write up the code

| Selector | Effect |
| --- | --- |
| `h3` and `a` | Targets elements of that HTML element type |
| `>` | Indicates a child element |
| `.price_color` and `article.product_pod` | Indicates a class name and, optionally, specifies on which element the class name should be |
| `::text` | Targets the text content of a HTML tag |
| `::attr(href)` | Targets the value of an HTML attribute, in this case the URL in an `href` attribute |

| Element | CSS Selector |
| --- | --- |
| Book elements | `article.product_pod` |
| URL | `h3 > a::attr(href)` |
| Title | `h3 > a::attr(title)` |
| Price | `.price_color::text` |

---

# Build Web Scrapper

- Create item classes to structure data
- Apply selectors to pinpoint the element that we want to extract
- Handle pagination to traverse multi-page datasets

## Collect the Data in an `Item`

`Item` is a Python map that can be used for validation and serialization. Defining an `Item` helps organize and standardized data that we want to scrape.

- Create a class that inherits from `scrapy.Item` and define the fields that we want to scrap as instances of `scrapy.field`

```python
import scrapy

class BooksItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field(
```

- `BooksItem` inherits from `Item`
- All other elements (`.url`, `.title`, `.price.`) defines as `Field`
    - `Field` class is a placeholder that's just an alias for Python Dict
    - It integrates with `Item` so it can be used to define fields that `Item` will contain

## Write a Scrapy Spider

Scrapy framework has a command (`genspider`) that creates a spider within the project. Make sure we `cd` into our project directory first

```bash
(venv) $ cd books/
(venv) $ scrapy genspider book https://books.toscrape.com/

```

- Pass in the target dir, and the target URL
- Scrapy creates a new file in the `spiders/` dir of the project
- It generates a class that inherits from `scrapy.Spider`
- 

**`parse()` method-**  a callback method that Scrapy calls with the downloaded response object for each URL 

- Finds all books on the current page and then iterates over each book
- For each book, it creates a `BooksItem` instance and extracts the URL, title, and price using CSS selectors
- Assigns these values to the respective fields of `BooksItem` and then yields the item instance to the item pipeline

## Extract Data From the Website

To run and execute the `spider`, run a Scrapy command

```python
scrapy crawl book
```

- Scrapy will crawl the specified URL and return logging information, including our extracted data for each book on the landing page

## Handle Pagination and Follow URLs

Create `pagination` so spider can navigate through multiple pages and extract data from each one.

[https://realpython.com/web-scraping-with-scrapy-and-mongodb/#:~:text=In the Books,HTML](https://realpython.com/web-scraping-with-scrapy-and-mongodb/#:~:text=In%20the%20Books,HTML)