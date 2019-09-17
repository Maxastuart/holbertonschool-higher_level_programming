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

	printf("before:\nfront= %d\n", runfront->n);
	printf("back= %d\n", runback->n);
	printf("len= %d\n\n", len);

	if (len == 1 || len == 0)
 	{
		printf("is it IF?\n");
		return (1);
	}
	else if (runfront->n != runback->n)
 	{
		printf("is it ELSE IF?\n");
		return (0);
	}
	runback = runfront;
	runfront = runfront->next;
	for (i = 0; i < len - 2; i++)
		runback = runback->next;
	len -= 2;

	printf("then:\nlen= %d\n", len);
	printf("front= %d\n", runfront->n);
	printf("back= %d\n", runback->n);

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

	for (len = 1; runback->next != NULL; len++) /* gets length of list */
		runback = runback->next;

	printf("head= %d\n", (*head)->n);
	printf("first runback= %d\n\n", runback->n);

	return (recur_pal(*head, runback, len));
}
