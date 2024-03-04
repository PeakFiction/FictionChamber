package main

import (
	"errors"
	"fmt"
)

var StudentList map[string]bool
var CourseList map[string]bool

func init() {
	StudentList = make(map[string]bool)
	CourseList = make(map[string]bool)
}

func AddStudent(studentID string, studentName string) (string, error) {
	if _, exists := StudentList[studentID]; exists {
		return "", errors.New(fmt.Sprintf("student %s is already in the list of students", studentID))
	}
	StudentList[studentID] = true
	return fmt.Sprintf("successfully added the student %s to the list of students", studentID), nil
}

func DropStudent(studentID string) (string, error) {
	if _, exists := StudentList[studentID]; !exists {
		return "", errors.New(fmt.Sprintf("student %s is not in the list of students", studentID))
	}
	delete(StudentList, studentID)
	return fmt.Sprintf("successfully removed student %s from the list of students", studentID), nil
}

func AddCourse(courseID string, courseName string, credit int) (string, error) {
	if _, exists := CourseList[courseID]; exists {
		return "", errors.New(fmt.Sprintf("course %s is already in the list of courses", courseID))
	}
	CourseList[courseID] = true
	return fmt.Sprintf("successfully added the course %s to the list of courses", courseID), nil
}

func DropCourse(courseID string) (string, error) {
	if _, exists := CourseList[courseID]; !exists {
		return "", errors.New(fmt.Sprintf("course %s is not in the list of courses", courseID))
	}
	delete(CourseList, courseID)
	return fmt.Sprintf("successfully removed the course %s from the list of courses", courseID), nil
}

func AddStudentCourse(studentID string, courseID string) (string, error) {
	if _, exists := StudentList[studentID]; !exists {
		return "", errors.New(fmt.Sprintf("student %s is not in the list of students", studentID))
	}
	if _, exists := CourseList[courseID]; !exists {
		return "", errors.New(fmt.Sprintf("course %s is not in the list of courses", courseID))
	}
	msg, err := Student.AddCourse(courseID)
	if err != nil {
		return "", err
	}
	msg, err = Course.AddStudent(studentID)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("successfully added the course %s for the student %s", courseID, studentID), nil
}

func DropStudentCourse(studentID string, courseID string) (string, error) {
	if _, exists := StudentList[studentID]; !exists {
		return "", errors.New(fmt.Sprintf("student %s is not in the list of students", studentID))
	}
	if _, exists := CourseList[courseID]; !exists {
		return "", errors.New(fmt.Sprintf("course %s is not in the list of courses", courseID))
	}
	msg, err := Student.DropCourse(courseID)
	if err != nil {
		return "", err
	}
	msg, err = Course.DropStudent(studentID)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("successfully removed the course %s from the student %s", courseID, studentID), nil
}

func PrintMessage(message string, err error) string {
	if err != nil {
		return fmt.Sprintf("[FAILED] %s", err.Error())
	}
	return fmt.Sprintf("[SUCCESS] %s", message)
}
