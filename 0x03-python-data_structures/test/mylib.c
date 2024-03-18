#include <stdio.h>
#include "Python.h"
void hello(void)
{
	printf("Hello, World!\n");
}

void print_list(PyObject *list)
{
	int i;
	PyListObject *_list;("Hello, list");
	_list = (PyListObject*)list;
	printf("[*] allocated = %ld\n", _list->allocated);
	printf("number of item = %ld\n", _list->ob_base.ob_size);
	for (i = 0; i < _list->ob_base.ob_size; i++)
	{
		printf("Item %i is a %s\n", i, _list->ob_item[i]->ob_type->tp_name);
	}
}
