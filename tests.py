from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    working = "ai_agent"
    directory = "functions"

    #Get files info tests
    '''result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("----------")
    print()

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("----------")
    print()

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("----------")
    print()

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("----------")
    print()

    result = get_files_info(working, directory)
    print(f"Result for '{directory}' directory:")
    print(result)
    print("----------")
    print()'''

    #Get file content lorem test
    '''result = get_file_content("calculator", "lorem.txt")
    print("Result for 'lorem.txt' file:")
    print(result)
    print("----------")
    print()'''

    #Get file content tests
    '''result = get_file_content("calculator", "main.py")
    print("Result for 'main.py' file:")
    print(result)
    print("----------")
    print()

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator.py' file:")
    print(result)
    print("----------")
    print()

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat' file:")
    print(result)
    print("----------")
    print()

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'pkg/does_not_exist.py' file:")
    print(result)
    print("----------")
    print()'''

    #Write file tests
    '''result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing to 'lorem.txt' file:")
    print(result)
    print("----------")
    print()

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing to 'pkg/morelorem.txt' file:")
    print(result)
    print("----------")
    print()

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing to '/tmp/temp.txt' file:")
    print(result)
    print("----------")
    print()'''

    #Run python file tests
    result = run_python_file("calculator", "main.py")
    print("Result for running 'main.py' file:")
    print(result)
    print("----------")
    print()

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for running 'main.py' file with args:")
    print(result)
    print("----------")
    print()

    result = run_python_file("calculator", "tests.py")
    print("Result for running 'tests.py' file:")
    print(result)
    print("----------")
    print()

    result = run_python_file("calculator", "../main.py") #should return an error
    print("Result for running '../main.py' file:")
    print(result)
    print("----------")
    print()

    result = run_python_file("calculator", "nonexistent.py") #should return an error
    print("Result for running 'nonexistent.py' file:")
    print(result)
    print("----------")
    print()

if __name__ == "__main__":
    test()   