class SegmentTree {
    struct Info {
        int l, r;
        char lc, rc;
        int len, lfreq, rfreq;
    };
    vector<Info> tree;
    int n;
    Info combine(const Info& a, const Info& b) {
        Info res;
        res.l = a.l;
        res.r = b.r;
        res.lc = a.lc;
        res.rc = b.rc;
        res.lfreq = a.lfreq;
        if (a.lfreq == a.r - a.l + 1 && a.rc == b.lc) res.lfreq += b.lfreq;
        res.rfreq = b.rfreq;
        if (b.rfreq == b.r - b.l + 1 && a.rc == b.lc) res.rfreq += a.rfreq;
        res.len = max({a.len, b.len});
        if (a.rc == b.lc) res.len = max(res.len, a.rfreq + b.lfreq);
        return res;
    }
    void build(const string& s, int i, int l, int r) {
        if (l == r) {
            tree[i] = {l, r, s[l], s[l], 1, 1, 1};
            return;
        }
        int m = (l + r) / 2;
        build(s, 2*i + 1, l, m);
        build(s, 2*i + 2, m + 1, r);
        tree[i] = combine(tree[2*i + 1], tree[2*i + 2]);
    }
    void update(int i, int l, int r, int idx, char c) {
        if (l == r) {
            tree[i] = {l, r, c, c, 1, 1, 1};
            return;
        }
        int m = (l + r) / 2;
        if (idx <= m) update(2*i + 1, l, m, idx, c);
        else update(2*i + 2, m + 1, r, idx, c);
        tree[i] = combine(tree[2*i + 1], tree[2*i + 2]);
    }
public:
    SegmentTree(const string& s) {
        n = s.size();
        tree.resize(4 * n);
        build(s, 0, 0, n - 1);
    }
    void modify(int idx, char c) {
        update(0, 0, n - 1, idx, c);
    }
    int longest() {
        return tree[0].len;
    }
};
class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        SegmentTree seg(s);
        vector<int> res;
        for (int i = 0; i < queryIndices.size(); ++i) {
            seg.modify(queryIndices[i], queryCharacters[i]);
            res.push_back(seg.longest());
        }
        return res;
    }
};