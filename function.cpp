#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> split_sentence(const std::string& sentence)
{
    std::vector<std::string> words;
    std::string word;
    std::istringstream iss(sentence);

    while (iss >> word)
    {
        words.push_back(word);
    }

    return words;
}

int main()
{
    std::string sentence;
    std::ifstream pipe_in("pipe_in", std::ios::in);
    std::ofstream pipe_out("pipe_out", std::ios::out);

    while (std::getline(pipe_in, sentence))
    {
        std::vector<std::string> words = split_sentence(sentence);
        for (const auto& word : words)
        {
            pipe_out << word << '\n';
        }
        pipe_out << std::flush;
    }

    return 0;
}