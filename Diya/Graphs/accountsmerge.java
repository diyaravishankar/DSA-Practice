class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        List<List<String>> ans = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        Disjoint ds = new Disjoint(accounts.size());

        // Iterate through accounts and union emails
        for (int i = 0; i < accounts.size(); i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String email = accounts.get(i).get(j);
                if (map.containsKey(email)) {
                    ds.union(i, map.get(email));
                } else {
                    map.put(email, i);
                }
            }
        }

        // Prepare lists for each account's emails
        ArrayList<String>[] emails = new ArrayList[accounts.size()];
        for (int i = 0; i < accounts.size(); i++) {
            emails[i] = new ArrayList<>();
        }

        // Assign emails to their ultimate parent account
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            emails[ds.findUparent(entry.getValue())].add(entry.getKey());
        }

        // Build the final answer
        for (int i = 0; i < accounts.size(); i++) {
            if (emails[i].size() == 0) continue;

            List<String> mergedAccount = new ArrayList<>();
            Collections.sort(emails[i]);
            mergedAccount.add(accounts.get(i).get(0)); // Add account name
            mergedAccount.addAll(emails[i]);
            ans.add(mergedAccount);
        }

        return ans;
    }
}

class Disjoint {
    ArrayList<Integer> parent = new ArrayList<>();
    ArrayList<Integer> size = new ArrayList<>();

    Disjoint(int n) {
        for (int i = 0; i < n; i++) {
            parent.add(i);
            size.add(1);
        }
    }

    public int findUparent(int node) {
        if (parent.get(node) != node) {
            int uP = findUparent(parent.get(node));
            parent.set(node, uP);
            return uP;
        }
        return node;
    }

    public void union(int x, int y) {
        int ux = findUparent(x);
        int uy = findUparent(y);

        if (ux == uy) return;
        if (size.get(ux) < size.get(uy)) {
            parent.set(ux, uy);
            size.set(uy, size.get(ux) + size.get(uy));
        } else {
            parent.set(uy, ux);
            size.set(ux, size.get(ux) + size.get(uy));
        }
    }
}