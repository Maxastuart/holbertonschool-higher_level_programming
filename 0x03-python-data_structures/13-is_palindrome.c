#include "lists.h"

/**
 * recur_pal - recursion helper function for is_palindrome
 * @runfront: pointer to the runner from the front of the listint_t list
 * @runback: pointer to the runner from the back of the listint_t list
 * @len: the remaining length of the list to check
 *
 * Return: 1 if palindrome, 0 if not.
 */
int recur_pal(listint_t *runfront, listint_t *runback, int len)
{
	int i;

	if (len == 1 || len == 0)
		return (1);
	else if (runfront->n != runback->n)
		return (0);
	runback = runfront;
	runfront = runfront->next;
	for (i = 0; i < len - 2; i++)
		runback = runback->next;
	len -= 2;

	return (recur_pal(runfront, runback, len));
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of a listint_t type list
 *
 * Return: 1 if it is a palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	int len;
	listint_t *runback = *head;

	if (*head == NULL)
		return (1);
	/* get len and set runback to last node */
	for (len = 1; runback->next != NULL; len++)
		runback = runback->next;

	return (recur_pal(*head, runback, len));
}
