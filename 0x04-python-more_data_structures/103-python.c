#include "Python.h"
#include <stdio.h>
/**
 * print_python_list - print python list info
 * @p: pointer to the object
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	int i;

	list = (PyListObject)p;

	printf("[*] Python List info\n");
	printf("[*] Size of the Python List = %lu\n", list->ob_base->ob_size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < list->ob_base->ob_size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}
/**
 * print_python_bytes - print information on strings
 * @p: pointer to the python object
 *
 * Return: nothing
 */
/* void print_python_bytes(PyObject *p) */
/* { */
/* 	PyBytesObject *by; */

/* 	by = (PyBytesObject)p; */

/* 	printf("[.] bytes object info\n"); */
/* 	printf("  size: %lu\n", by->ob_base->ob_size); */
/* 	printf("  trying string: %s\n", ); */
/* 	printf("  first %d bytes: \n", ); */
