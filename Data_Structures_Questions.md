Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`? O(1)

2. What is the runtime complexity of `dequeue`? O(1)

3. What is the runtime complexity of `len`? O(n)

## Binary Search Tree

1. What is the runtime complexity of `insert`? log(n)

2. What is the runtime complexity of `contains`? log(n)

3. What is the runtime complexity of `get_max`? log(n)

## Heap

1. What is the runtime complexity of `_bubble_up`? logb2(n) - 1 --> logb2(n)

2. What is the runtime complexity of `_sift_down`? log(n)

3. What is the runtime complexity of `insert`? logb2(n)

4. What is the runtime complexity of `delete`? log(n)

5. What is the runtime complexity of `get_max`? O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(1)

2. What is the runtime complexity of `ListNode.insert_before`? O(1)

3. What is the runtime complexity of `ListNode.delete`? O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    Splice's worst case is O(n), delete is O(1)
