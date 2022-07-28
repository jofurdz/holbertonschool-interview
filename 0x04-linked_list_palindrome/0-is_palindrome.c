#include "lists.h"
/**
 * recurse_list - recursive function for comparing nodes
 *
 * @left: nodes for left of list
 * @right: nodes for the right
 *
 * Return: 0 if not palindrome and 1 if palindrome
 */


int recurse_list(listint_t **left, listint_t *right)
{
	int poopla;

	if (right == NULL)
	{
		return (1);
	}

	poopla = recurse_list(left, right->next) && (*left)->n == right->n;
	*left = (*left)->next;

	return (poopla);
}

/**
 * is_palindrome - checks if linked list is palindrome
 *
 * @head: double pointer to head of list
 * Return: 0 if not palindrome and 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *newList = *head;

	return (recurse_list(&newList, newList));
}
