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
	int num_node = 0;
        int *t, i, j;

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
	i = 0;
	tmp = *head;
	while (i != num_node)
	{
		t[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	j = num_node - 1;
	i = 0;
	while(i != num_node/2)
	{
		if (t[i] != t[j])
			return (0);

		i++;
		j--;
	}
	return (1);
}
