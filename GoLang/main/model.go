package main

import (
	"errors"
	"fmt"
)

// Tool interface defines methods for Student and Course structs
type Tool interface {
	Add(any) error
	Drop(any) error
	Get() string
	GetArray() []string
}

// Student struct stores student information
type Student struct {
	name         string
	id           string
	addedCourses map[string]bool
}

// Add method adds the course id into the courses taken by student
func (s *Student) Add(courseID string) error {
	if _, exists := s.addedCourses[courseID]; exists {
		return errors.New(fmt.Sprintf("course %s has been taken by the student %s", courseID, s.id))
	}
	s.addedCourses[courseID] = true
	return nil
}

// Drop method removes the course id from the courses taken by student
func (s *Student) Drop(courseID string) error {
	if _, exists := s.addedCourses[courseID]; !exists {
		return errors.New(fmt.Sprintf("course %s has not been taken by the student %s", courseID, s.id))
	}
	delete(s.addedCourses, courseID)
	return nil
}

// Get method returns student ID
func (s *Student) Get() string {
	return s.id
}

// GetArray method returns the list of courses taken by the student
func (s *Student) GetArray() []string {
	courses := make([]string, 0, len(s.addedCourses))
	for course := range s.addedCourses {
		courses = append(courses, course)
	}
	return courses
}

// Course struct stores course information
type Course struct {
	name             string
	id               string
	capacity         int
	studentsInCourse map[string]bool
}

// Add method adds a student ID to the list of students who have enrolled in the course
func (c *Course) Add(studentID string) error {
	if len(c.studentsInCourse) >= c.capacity {
		return errors.New(fmt.Sprintf("enrollment capacity for the course %s has already been reached", c.id))
	}
	if _, exists := c.studentsInCourse[studentID]; exists {
		return errors.New(fmt.Sprintf("student %s has already taken the course %s", studentID, c.id))
	}
	c.studentsInCourse[studentID] = true
	return nil
}

// Drop method removes the course ID from the list of courses taken by the student
func (c *Course) Drop(studentID string) error {
	if _, exists := c.studentsInCourse[studentID]; !exists {
		return errors.New(fmt.Sprintf("student %s did not take the course %s", studentID, c.id))
	}
	delete(c.studentsInCourse, studentID)
	return nil
}

// Get method returns course ID
func (c *Course) Get() string {
	return c.id
}

// GetArray method returns the list of students who have enrolled in the course
func (c *Course) GetArray() []string {
	students := make([]string, 0, len(c.studentsInCourse))
	for student := range c.studentsInCourse {
		students = append(students, student)
	}
	return students
}
