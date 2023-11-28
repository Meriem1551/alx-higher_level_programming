#include "lists.h"
/**
 * insert_node - adds node in a specific position
 * @head: pointer to a struct
 * @number: number to insert
 * Return: @ of new node else NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *tmp, *q = NULL, *new;
if (*head == NULL)
	return NULL;
new = (listint_t *)malloc(sizeof(listint_t));
if (new == NULL)
	return NULL;
new->n = number;
new->next = NULL;
tmp = *head;
while (tmp != NULL && number > tmp->n)
{
	q = tmp;
	tmp = tmp->next;
}
new->next = q->next;
q->next = new;
return (new);
}
