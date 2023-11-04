#!/usr/bin/env bash

# These are my gut repositories
gitRepos=(
    $HOME/.config/dot-files/
    $HOME/Documents/lab/curriculum
    $HOME/Documents/lab/fisica-geral/
    $HOME/Documents/lab/portfolio/
    $HOME/Documents/lab/research-projects/
    $HOME/Documents/lab/scripts-and-snippets/
    $HOME/Documents/lab/wiki/
    $HOME/Documents/lab/work/spectral-curves/
    $HOME/Documents/lab/work/spin-chains/
)

for repo in "${gitRepos[@]}"
do
    test -n "$(git -C $repo status --porcelain)" && echo ">> MODIFIED :: $repo" #|| echo "<< NOTHING :: $repo"
done

   
