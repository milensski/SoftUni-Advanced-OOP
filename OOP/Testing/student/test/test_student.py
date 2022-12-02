from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('Milen')
        self.student_with_course = Student('Ivan', {'math': ['note']})

    def test_init_method(self):
        self.assertEqual('Milen', self.student.name)
        self.assertEqual({},self.student.courses)
        self.assertEqual({'math': ['note']},self.student_with_course.courses)

    def test_enroll_if_course_already_exists(self):
        notes = ['note2', 'note3']
        result = self.student_with_course.enroll('math',notes)
        self.assertEqual(['note','note2', 'note3'],self.student_with_course.courses['math'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_if_course_not_exist_and_add_course_notes(self):
        notes = ['note2', 'note3']
        result = self.student.enroll('bio', notes)
        self.assertEqual(['note2', 'note3'],self.student.courses['bio'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_if_course_not_exist_and_add_course_notes_with_param_y(self):
        notes = ['note2', 'note3']
        result = self.student.enroll('bio', notes, "Y")
        self.assertEqual(['note2', 'note3'],self.student.courses['bio'])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_only_course(self):
        result = self.student.enroll('math', 'note1', "N")
        self.assertEqual({'math': []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_in_course(self):
        result = self.student_with_course.add_notes('math', 'note2')
        self.assertEqual(['note','note2'],self.student_with_course.courses['math'])
        self.assertEqual("Notes have been updated",result)

    def test_add_notes_without_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', 'note2')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.student_with_course.leave_course('math')
        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_unexisting_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()