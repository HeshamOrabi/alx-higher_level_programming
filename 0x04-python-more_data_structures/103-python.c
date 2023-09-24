#include <Python.h>
#include <object.h>
#include <listobject.h>


/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
*/
void print_python_bytes(PyObject *p)
{
	long int size, i, limit;
	char *string;

	if (PyBytes_Check(p))
	{
		size = ((PyVarObject *)(p))->ob_size;
		string = ((PyBytesObject *)p)->ob_sval;
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list_info - Prints information about a Python list object.
 * @p: A pointer to a Python object.
*/
void print_python_list(PyObject *p)
{
	long int size;
	int i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Not a list object\n");
		exit(EXIT_FAILURE);
	}

	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}

}
