#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - Prints all elements of a listint_t list.
 * @h: Pointer to the head of the list.
 * Return: Number of nodes.
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current = h;
    size_t count = 0;

    while (current)
    {
        printf("%d\n", current->n);
        current = current->next;
        count++;
    }

    return count;
}

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 * @head: Pointer to a pointer of the start of the list.
 * @n: Integer to be included in the new node.
 * Return: Address of the new element or NULL if it fails.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return NULL;

    new_node->n = n;
    new_node->next = *head;
    *head = new_node;

    return new_node;
}

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to the list to be freed.
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

