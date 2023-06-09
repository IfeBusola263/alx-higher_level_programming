#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the head pointer
 * Return: returns 1 on success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptrTop, *ptrMid;
	listint_t *ptr_p, *ptr_n, *ptr_c;

	if (*head != NULL && (*head)->next != NULL)
	{
		ptrTop = *head;
		ptrMid = *head;

		while (ptrTop && ptrTop->next) /* get to the middle */
		{
			ptrTop = ptrTop->next->next;
			ptrMid = ptrMid->next;
		}

		ptrTop = *head;
		ptr_p = NULL;
		ptr_n = ptrMid->next->next;
		ptr_c = ptrMid->next;
		while (ptr_n) /* reverse the list from the middle downwards */
		{
			ptr_c->next = ptr_p;
			ptr_p = ptr_c;
			ptr_c = ptr_n;
			ptr_n = ptr_c->next;
		}
		ptrMid->next = ptr_c;
		ptr_c->next = ptr_p;
		ptrMid = ptrMid->next;
		while (ptrMid) /* compare the items for similarity or diff */
		{
			if (ptrTop->n != ptrMid->n)
				return (0);
			ptrMid = ptrMid->next;
			ptrTop = ptrTop->next;
		}
		return (1);
	}
	return (1);
}
