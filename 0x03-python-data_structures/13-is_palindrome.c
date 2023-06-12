#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the head pointer
 *
 * Return: returns 1 at success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptrTop, *ptrMid;
	int arr[100], i, len;

	if (head != NULL)
	{
		ptrTop = *head;
		ptrMid = *head;

		i = 0;
		while (ptrTop && ptrTop->next)
		{
			arr[i] = ptrMid->n;
			ptrTop = ptrTop->next->next;
			ptrMid = ptrMid->next;
			i++;
		}
		len = i;
		ptrTop = *head;

		for (i = 0; i < len ; i++)
		{
			if (arr[i] != ptrTop->n)
				return (0);
			ptrTop = ptrTop->next;
		}
		return (1);
	}
	return (1);
}
