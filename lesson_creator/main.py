# Creator a folder with a lesson content format
# Parent folder (ex: Ch_01)
# Child folder (Takes user input) (ex: child -3 = ch_01, ch_02, ch_03)
# Pass in topic, Use ChatGPT prompt to give a lesson structure based on how many child folder

# Create an optional function to create an entire lesson plan/structure on a topic.

# Functions
# folder_creator()
# gpt_summarize()


import gpt_create

def create_chapter(topic, custom_content=""):
    chapter_content =  gpt_create.chapter_content(topic, custom_content)


    # Check if lesson content is empty
    if chapter_content.strip():
        lesson_file = "CHAPTER.MD"
        try:
            with open(lesson_file, "w") as file:
                file.write(chapter_content)
        except Exception as e:
            print (f"An error occured while writing to the file: {e}")
    else:
        print ("No content to write to the file")

def create_lesson_structure(topic, custom_content=""):
    lesson_structure =  gpt_create.lesson_structure(topic, custom_content)


    # Check if lesson content is empty
    if lesson_structure.strip():
        lesson_structure_file = "LESSON_STRUCTURE.MD"
        try:
            with open(lesson_structure_file, "w") as file:
                file.write(lesson_structure)
        except Exception as e:
            print (f"An error occured while writing to the file: {e}")
    else:
        print ("No content to write to the file")

def main():
    create_chapter("Terraform workspace", "Provide some helpful links to relatable docs at the end of the chapter")
    # create_lesson_structure("Terraform")



if __name__ == "__main__":
    main()
