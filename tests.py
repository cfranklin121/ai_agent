from functions.get_files_info import get_files_info

def test():
    working = "ai_agent"
    directory = "functions"

    result = get_files_info("calculator", ".")
    print(result)
    print("----------")
    print()

    result = get_files_info("calculator", "pkg")
    print(result)
    print("----------")
    print()

    result = get_files_info("calculator", "/bin")
    print(result)
    print("----------")
    print()

    result = get_files_info("calculator", "../")
    print(result)
    print("----------")
    print()

    result = get_files_info(working, directory)
    print(result)
    print("----------")
    print()

if __name__ == "__main__":
    test()   