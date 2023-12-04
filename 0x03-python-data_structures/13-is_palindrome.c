#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a list is palidrom
 * @head: pointer to a list
 * Return: 1 if it's palindromm, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int num_node = 0, *t, i = 0, j = 0;

	if (*head == NULL)
		return (1);
	tmp = *head;
	num_node = 0;
	while(tmp != NULL)
	{
		num_node++;
		tmp = tmp->next;
	}
	t = (int *)malloc(sizeof(int) * num_node);
	tmp = *head;
	while (i != num_node)
	{
		t[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	i--;
	while(j != num_node/2)
	{
		if (t[j] != t[i])
			return (0);

		j++;
		i--;
	}
	return (1);
}
