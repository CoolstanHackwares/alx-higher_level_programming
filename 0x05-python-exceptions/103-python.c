#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

/**
 * print_python_list - A funnction that prints information about a Python list
 * @p: A pointer to the Python list object
 * This program conforms to the betty documentation style
 **/

void print_python_list(PyObject *p)
{
	long unsigned int size;
	unsigned int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	if (!PyList_Check(list))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
		if (!strcmp(type, "float"))
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - A function that prints information about a Python
 * bytes object
 * @p: A pointer to the Python bytes object
 * This program conforms to the betty documentation style
 **/

void print_python_bytes(PyObject *p)
{
	long unsigned int size;
	unsigned int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	trying_str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", trying_str);
	printf("  first %lu bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i < 10 && i < size; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * print_python_float - A function that prints information about
 * a Python float object
 * @p: A pointer to the Python float object
 * This program conforms to the betty documentation style
 **/

void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double d = f->ob_fval;
	char *str = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(f))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
