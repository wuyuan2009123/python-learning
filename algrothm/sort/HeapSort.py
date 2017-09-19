#!/usr/bin/env python3

"""选择排序—堆排序（Heap Sort） 时间复杂度 O(nlogn)
    堆排序是一种树形选择排序，是对直接选择排序的有效改进。
    
    基本思想：
    
    堆的定义如下：具有n个元素的序列（k1,k2,...,kn),当且仅当满足
        最小堆：Ki <= K2i and Ki <= K(2i+1)   
        最大堆：Ki >= K2i and Ki >= K(2i+1)
    时称之为堆。由堆的定义可以看出，堆顶元素（即第一个元素）必为最小项（小顶堆）。
    若以一维数组存储一个堆，则堆对应一棵完全二叉树，且所有非叶结点的值均不大于(或不小于)其子女的值，根结点（堆顶元素）的值是最小(或最大)的。如：
        （a）大顶堆序列：（96, 83,27,38,11,09)
         (b) 小顶堆序列：（12，36，24，85，47，30，53，91）
    初始时把要排序的n个数的序列看作是一棵顺序存储的二叉树（一维数组存储二叉树），调整它们的存储序，使之成为一个堆，将堆顶元素输出，得到n 个元素中最小（或最大）的元素，这时堆的根节点的数最小（或者最大）。然后对前面(n-1)个元素重新调整使之成为堆，输出堆顶元素，得到n 个元素中次小(或次大)的元素。依此类推，直到只有两个节点的堆，并对它们作交换，最后得到有n个节点的有序序列。称这个过程为堆排序。
    因此，实现堆排序需解决两个问题：
        1. 如何将n 个待排序的数建成堆；
        2. 输出堆顶元素后，怎样调整剩余n-1 个元素，使其成为一个新堆。
    首先讨论第二个问题：输出堆顶元素后，对剩余n-1元素重新建成堆的调整过程。
    调整小顶堆的方法：
        1）设有m 个元素的堆，输出堆顶元素后，剩下m-1 个元素。将堆底元素送入堆顶（（最后一个元素与堆顶进行交换），堆被破坏，其原因仅是根结点不满足堆的性质。
        2）将根结点与左、右子树中较小元素的进行交换。 
        3）若与左子树交换：如果左子树堆被破坏，即左子树的根结点不满足堆的性质，则重复方法 （2）.
        4）若与右子树交换，如果右子树堆被破坏，即右子树的根结点不满足堆的性质。则重复方法 （2）.
        5）继续对不满足堆性质的子树进行上述交换操作，直到叶子结点，堆被建成。
        这个自根结点到叶子结点的调整过程为筛选。
    再讨论对n 个元素初始建堆的过程。
    建堆方法：对初始序列建堆的过程，就是一个反复进行筛选的过程。
        1）n 个结点的完全二叉树，则最后一个结点是第n/2个结点的子树。
        2）筛选从第n/2个结点为根的子树开始，该子树成为堆。
        3）之后向前依次对各结点为根的子树进行筛选，使之成为堆，直到根结点。
                                  
     算法的实现：
    
    从算法描述来看，堆排序需要两个过程，一是建立堆，二是堆顶与堆的最后一个元素交换位置。所以堆排序有两个函数组成。一是建堆的渗透函数，二是反复调用渗透函数实现排序的函数。
    :author Wang Weiwei <email>weiwei02@vip.qq.com / weiwei.wang@100credit.com</email> 
    :sine 2017/9/2
    :version 1.0
"""


def adjust_heap(arr, top, length):
    """
    调整 arr[top] 为大顶堆，即将以第top个元素为根节点的子树重构
    
    :param arr: 待调整的数组
    :param top: 根节点
    :param length: 数组长度
    :return: void
    """
    temp = arr[top]
    # 左孩子节点的索引  由于数组索引为
    chirld = top * 2 + 1
    # 上游方法已经对length做了控制 arr[length] 为可取值的状态
    while chirld < length:
        if chirld < length - 1 and arr[chirld] < arr[chirld + 1]:
            chirld += 1
        if arr[chirld] > arr[top]:
            # 如果较大的子节点大于父节点，则将子节点向上移动
            arr[top] = arr[chirld]
            arr[chirld] = temp
            top = chirld
            chirld = top * 2 + 1
        else:
            break


def built_heap(arr):
    """初始化堆，即逐个调整每个有孩子节点的元素的位置"""
    # 最后一个有孩子节点的位置
    end = (len(arr) - 1) // 2
    while end >= 0:
        adjust_heap(arr, end, len(arr) - 1)
        end -= 1


def heap_sort(arr):
    """
    堆排序
    步骤：
    1.初始化大顶堆
    2.把大顶堆的根元素和数组末尾的元素交换（大顶堆条件被破坏），数组尾指针向前移动一位，然后重构堆
    3.重复2，直到堆中不再有元素
    4.从小到大排序的数组完成
    :param arr: 
    :return: 
    """
    built_heap(arr)
    # 堆空间
    end = len(arr) - 1
    while end > 0:
        temp = arr[end]
        arr[end] = arr[0]
        arr[0] = temp
        adjust_heap(arr, 0, end)
        end -= 1


if __name__ == '__main__':
    arr1 = [1, 5, 2, 4, 0, 14, 42, 65, 27, 22]
    print('元集合', arr1)
    heap_sort(arr1)
    print('新集合', arr1)