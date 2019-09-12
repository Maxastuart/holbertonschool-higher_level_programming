#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node in the appropriate place in a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new, *current;

  current = *head;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;

  if (*head == NULL)
    {
      *head = new;
      new->next = NULL;
    }
  else
    {
      while ((current->next != NULL) &&
	     !((current->n <= number) && (current->next->n >= number)))
	{
	  current = current->next;
	}
      if (current->next == NULL)
	{
	  new->next = NULL;
	}
      else
	{
	  new->next = current->next;
	}
      current->next = new;
    }

  return (new);
}
