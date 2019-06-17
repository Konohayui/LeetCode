/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var addTwoNumbers = function(l1, l2) {
    var temp = new ListNode(0);
    var head = temp;
    var carry = 0;
    
    while (l1 !== null || l2 !== null || carry > 0){
        if (l1 !== null) {
            carry = carry + l1.val;
            l1 = l1.next;
        }
        
        if (l2 !== null) {
            carry = carry + l2.val;
            l2 = l2.next;
        }
        
        head.next = new ListNode(carry%10);
        head = head.next;
        carry = Math.floor(carry/10);
        
    }
    return temp.next;
    
};
