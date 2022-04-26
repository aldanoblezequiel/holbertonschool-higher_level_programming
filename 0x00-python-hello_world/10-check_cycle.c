#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *y, *z;

	if (list == NULL || list->next == NULL)
		return (0);

	y = list->next;
	z = list->next->next;

	while (y && z && z->next)
	{
		if (y == z)
			return (1);
		y = y->next;
		z = z->next->next;
	}
	return (0);
}
