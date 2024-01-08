#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - A function that prints some basic info
 * about Python lists
 * @p: pointer to the pyobject
 * This program conforms to the betty documentation style
 **/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < size; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[i])->tp_name);
}
