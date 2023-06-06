#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts number into sorted linked list
 * @head: pointer to the head pointer
 * @number: number to be add
 *
 * Return: returns address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1;
	listint_t *ptr2;
	listint_t *newNode;

	if (*head != NULL)
	{
		ptr1 = *head;
		ptr2 = *head;
		newNode = malloc(sizeof(listint_t));
		if (newNode == NULL)
			return (NULL);

		newNode->n = number;
		if (ptr1->n > number)
		{
			*head = newNode;
			newNode->next = ptr1;
			return (newNode);
		}
		while (ptr1->next)
		{
			ptr1 = ptr1->next;
			if ((ptr2->n < number) && (number < ptr1->n))
			{
				ptr2->next = newNode;
				newNode->next = ptr1;
				return (newNode);
			}
			ptr2 = ptr2->next;
		}
		ptr2->next = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	return (NULL);
}
