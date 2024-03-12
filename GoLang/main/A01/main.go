package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	run()
}

func run() {
	fmt.Println("Welcome to the student course management system!")
	fmt.Println("Available commands:")
	fmt.Println("ADD_STUDENT [STUDENT_NAME] [STUDENT_ID]")
	fmt.Println("DROP_STUDENT [STUDENT_ID]")
	fmt.Println("ADD_COURSE [COURSE_NAME] [COURSE_ID] [CAPACITY]")
	fmt.Println("DROP_COURSE [COURSE_ID]")
	fmt.Println("ADD_STUDENT_COURSE [STUDENT_ID] [COURSE_ID]")
	fmt.Println("DROP_STUDENT_COURSE [STUDENT_ID] [COURSE_ID]")
	fmt.Println("EXIT")

	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Print("> ")
		scanner.Scan()
		input := scanner.Text()
		args := strings.Fields(input)

		if len(args) == 0 {
			continue
		}

		switch args[0] {
		case "ADD_STUDENT":
			if len(args) < 3 {
				fmt.Println("Usage: ADD_STUDENT [STUDENT_NAME] [STUDENT_ID]")
				continue
			}
			message, err := AddStudent(args[2], args[1])
			fmt.Println(PrintMessage(message, err))

		case "DROP_STUDENT":
			if len(args) < 2 {
				fmt.Println("Usage: DROP_STUDENT [STUDENT_ID]")
				continue
			}
			message, err := DropStudent(args[1])
			fmt.Println(PrintMessage(message, err))

		case "ADD_COURSE":
			if len(args) < 4 {
				fmt.Println("Usage: ADD_COURSE [COURSE_NAME] [COURSE_ID] [CAPACITY]")
				continue
			}
			capacity := 0
			fmt.Sscanf(args[3], "%d", &capacity)
			message, err := AddCourse(args[2], args[1], capacity)
			fmt.Println(PrintMessage(message, err))

		case "DROP_COURSE":
			if len(args) < 2 {
				fmt.Println("Usage: DROP_COURSE [COURSE_ID]")
				continue
			}
			message, err := DropCourse(args[1])
			fmt.Println(PrintMessage(message, err))

		case "ADD_STUDENT_COURSE":
			if len(args) < 3 {
				fmt.Println("Usage: ADD_STUDENT_COURSE [STUDENT_ID] [COURSE_ID]")
				continue
			}
			message, err := AddStudentCourse(args[1], args[2])
			fmt.Println(PrintMessage(message, err))

		case "DROP_STUDENT_COURSE":
			if len(args) < 3 {
				fmt.Println("Usage: DROP_STUDENT_COURSE [STUDENT_ID] [COURSE_ID]")
				continue
			}
			message, err := DropStudentCourse(args[1], args[2])
			fmt.Println(PrintMessage(message, err))

		case "EXIT":
			fmt.Println("Exiting program...")
			return

		default:
			fmt.Println("Invalid command. Please try again.")
		}
	}
}
