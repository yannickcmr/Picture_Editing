#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "introprog_telefonbuch.h"

/*
 * Fügt einen Knoten mit der Telefonnummer phone und dem Namen name
 * in den Binären Suchbaum bst ein.  Für den Suchbaum soll die
 * Eigenschaft gelten, dass alle linken Kinder einen Wert kleiner
 * gleich (<=) und alle rechten Kinder einen Wert größer (>) haben.
 */
void bst_insert_node(bstree* bst, unsigned long phone, char *name) {
    bst_node* new_node = malloc(sizeof(bst_node));
    new_node->name = name;
    new_node->phone = phone;

    if (bst->root == NULL){
        bst->root = new_node;
    } 
    bst_node* cache = bst->root;
    bst_node* parent;

    while (cache != NULL){
        parent = cache;
        if (cache->phone < phone){
            cache = cache->right;
        } else {
            cache = cache->left;
        }
    }

    if (parent->phone < phone){
        parent->right = new_node;
    } else {
        parent->left = new_node;
    }
}

bst_node* recursiveSearch(bst_node* node, unsigned long key){
    if (node == NULL){
        return NULL;
    } else if (node->phone == key){
        return node;
    };
    if (node->phone > key){
        return recursiveSearch(node->left, key);
    } else {
        return recursiveSearch(node->right, key);
    }
}

/*
 * Diese Funktion liefert einen Zeiger auf einen Knoten im Baum mit
 * dem Wert phone zurück, falls dieser existiert.  Ansonsten wird
 * NULL zurückgegeben.
 */
bst_node* find_node(bstree* bst, unsigned long phone) {
    return recursiveSearch(bst->root, phone);
    }

/* Gibt den Unterbaum von node in "in-order" Reihenfolge aus */
void bst_in_order_walk_node(bst_node* node) {
    if (node != NULL){
        bst_in_order_walk_node(node->left);
        print_node(node);
        bst_in_order_walk_node(node->right);
    }
}

/* 
 * Gibt den gesamten Baum bst in "in-order" Reihenfolge aus.  Die
 * Ausgabe dieser Funktion muss aufsteigend soriert sein.
 */
void bst_in_order_walk(bstree* bst) {
    if (bst != NULL) {
        bst_in_order_walk_node(bst->root);
    }
}

/*
 * Löscht den Teilbaum unterhalb des Knotens node rekursiv durch
 * "post-order" Traversierung, d.h. zurerst wird der linke und dann
 * der rechte Teilbaum gelöscht.  Anschließend wird der übergebene
 * Knoten gelöscht.
 */
void bst_free_subtree(bst_node* node) {
    if (node->left != NULL){
        bst_free_subtree(node->left);
    } 
    
    if (node->right != NULL){
        bst_free_subtree(node->right);
    }
    free(node);
}

/* 
 * Löscht den gesamten Baum bst und gibt den entsprechenden
 * Speicher frei.
 */
void bst_free_tree(bstree* bst) {
    if(bst != NULL && bst->root != NULL) {
        bst_free_subtree(bst->root);
        bst->root = NULL;
    }
}
