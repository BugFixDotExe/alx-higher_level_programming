#include "lists.h"

/**
 * check_cycle - a function that checks a linked
 * list for a cycle
 * @list: the list to be checked
 * Return: a 1 if a cycle and 0 if not a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head_addr;
	listint_t *current_node;


	current_node = list;
	head_addr = list;
	if (list == NULL)
		return (0);
	while (current_node != NULL)
	{
		if (current_node->next == NULL)
		{
			return (0);
		}
		else
		{
			if (current_node->next == head_addr)
				return (1);
			current_node = current_node->next;
		}
	}
	return (0);
}
