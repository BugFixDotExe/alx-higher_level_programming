#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - a function that runs
 * a python print python objects info
 * form a C file
 * @p: a pointer of type PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *_list;
	_list = (PyListObject *) p;
	printf("[*] Size of the Python List = %ld\n", _list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", _list->allocated);
	for (i = 0; i < _list->ob_base.ob_size; i++)
	{
		printf("Element %i: %s\n", i, _list->ob_item[i]->ob_type->tp_name);
	}
}
