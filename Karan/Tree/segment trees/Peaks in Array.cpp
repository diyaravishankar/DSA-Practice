class SegmentTree
{
private:
    int n;
    vector<int> arr;
    vector<int> tree;
    bool isPeak(int index)
    {
        if (index == 0 || index == n - 1)
            return false;
        return (arr[index] > arr[index - 1]) && (arr[index] > arr[index + 1]);
    }
    void buildSegmentTree(int index, int left, int right)
    {
        if (left == right)
        {
            tree[index] = isPeak(left);
            return;
        }
        int mid = (left + right) / 2;
        buildSegmentTree(2 * index + 1, left, mid);
        buildSegmentTree(2 * index + 2, mid + 1, right);
        tree[index] = tree[2 * index + 1] + tree[2 * index + 2];
    }
    int querySegmentTree(int arrayLeft, int arrayRight, int treeLeft, int treeRight, int treeIndex)
    {
        if (treeRight < arrayLeft || treeLeft > arrayRight)
            return 0;
        if (treeLeft >= arrayLeft && treeRight <= arrayRight)
            return tree[treeIndex];
        int mid = (treeLeft + treeRight) / 2;
        int left = querySegmentTree(arrayLeft, arrayRight, treeLeft, mid, 2 * treeIndex + 1);
        int right = querySegmentTree(arrayLeft, arrayRight, mid + 1, treeRight, 2 * treeIndex + 2);
        return (left + right);
    }
    void updateSegmentTree(int arrayIndex, int newVal, int treeLeft, int treeRight, int treeIndex)
    {
        if (treeLeft == treeRight)
        {
            tree[treeIndex] = isPeak(arrayIndex);
            return;
        }
        int mid = (treeLeft + treeRight) / 2;
        if (mid >= arrayIndex)
            updateSegmentTree(arrayIndex, newVal, treeLeft, mid, 2 * treeIndex + 1);
        else
            updateSegmentTree(arrayIndex, newVal, mid + 1, treeRight, 2 * treeIndex + 2);
        tree[treeIndex] = tree[2 * treeIndex + 1] + tree[2 * treeIndex + 2];
    }
public:
    SegmentTree(vector<int> &nums)
    {
        arr = nums;
        n = arr.size();
        tree.resize(4 * n);
        buildSegmentTree(0, 0, n - 1);
    }

    int query(int left, int right)
    {
        return querySegmentTree(left, right, 0, n - 1, 0);
    }

    void update(int index, int val)
    {
        arr[index] = val;
        updateSegmentTree(index, val, 0, n - 1, 0);
        if (index > 0)
            updateSegmentTree(index - 1, arr[index - 1], 0, n - 1, 0);
        if (index < n - 1)
            updateSegmentTree(index + 1, arr[index + 1], 0, n - 1, 0);
    }
};
class Solution
{
public:
    vector<int> countOfPeaks(vector<int> &nums, vector<vector<int>> &queries)
    {
        SegmentTree ST(nums);
        vector<int> res;
        for (vector<int> q : queries)
        {
            if (q[0] == 1)
            {
                int l = q[1];
                int r = q[2];
                int val = ST.query(l + 1, r - 1);
                res.push_back(val);
            }
            else
                ST.update(q[1], q[2]);
        }
        return res;
    }
};