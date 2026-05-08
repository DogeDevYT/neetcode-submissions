

class Solution {
public:

    /*
    For this solution, we will use a delimiter approach such that we store the length of the encoded string
    and the delimiter "#" in this case, to then encode with length of string and then delimiter itself
    and then the actual string repeated for every string in the array

    so it would look like 

    cat, hat, rat

    3#cat3#hat3#rat
    */

    string encode(vector<string>& strs) {
        std::string solution = "";

        for (std::string str : strs) 
        {
            std::string current = "";
            int length = str.size();

            current += std::to_string(length); //if we dont add this we're going to be adding
            //ASCII equivalent
            current += "#";
            current += str;

            solution += current;
        }

        return solution;
    }

    vector<string> decode(string s) {
        int index = 0; 
        std::vector<std::string> solution;

        //iterate while we keep finding our delimiter
        while (index < s.size()) 
        {
            //find where length ends
            int j = s.find("#", index);

            //extract substring length
            int length = stoi(s.substr(index, j-index));

            //move index ot start of actual string
            index = j + 1;

            //extract the word and add to list
            solution.push_back(s.substr(index, length)); //second arrgument here is number of characters

            //move index
            index += length;
        }

        return solution;
    }
};
