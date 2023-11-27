#include "lists.h"

/**
 * check_cycle - checks if there si a cycle
 * @list: pointer to a list
 * Return: 1 if there is 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;
	if (list == NULL)
		return (0);
	tmp = list;
	while (tmp->next != NULL)
	{
		if (tmp->next == list)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
