/**
 * Created by Chasel on 2017/3/31.
 */


function ListNode(val) {
    this.val = val;
    this.next = null;
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var first,p,q,r;
    if (head==null){
        return null;
    }
    first=head;
    p=head;
    if (p.next==null){
        return p;
    }
    q=p.next;
    if (q.next==null){
        q.next=p;
        p.next=null;
        return q;
    }
    r=q.next;
    while (r!=first&&r!=null){
        q.next=p;
        p=q;
        q=r;
        r=r.next;
    }
    if (r==null){
        q.next=p;
        head.next=null;
        return q;
    }
    else {
        r.next=q;
        q.next=p;
        return r;
    }
};
var node1=new ListNode(1);
var node2=new ListNode(2);
var node3=new ListNode(3);
var node4=new ListNode(4);
node1.next=node2;
node2.next=node3;
node3.next=node4;
//node4.next=node1;
console.log(reverseList(null));