#include <stdio.h>
#include <stdlib.h>

/* Structure for a singly linked list node */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *tmp, *mid;
	slow = fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* If the length is odd, ignore the middle element */
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	prev->next = NULL;
	tmp = NULL;
	while (slow != NULL)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	/* Compare the reversed second half with the first half */
	tmp = prev;
	slow = *head;
	while (tmp != NULL)
	{
		if (slow->n != tmp->n)
			return 0;
		slow = slow->next;
		tmp = tmp->next;
	}

	return 1;
}
