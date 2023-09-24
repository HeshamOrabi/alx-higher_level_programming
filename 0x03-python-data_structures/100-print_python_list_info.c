#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about a Python list object.
 * @p: A pointer to a Python object.
*/
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Not a list object\n");
		exit(EXIT_FAILURE);
	}

	printf("[*] Size of the Python List = %ld", size);
	printf("[*] Allocated = %ld", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
