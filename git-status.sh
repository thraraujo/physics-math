#!/usr/bin/env bash

# These are my git repositories
gitRepos=(
    $HOME/.config/dot-files/
    $HOME/Documents/projects/aulas/
    $HOME/Documents/projects/cv-projects-documents/
    $HOME/Documents/projects/fisica-geral/
    $HOME/Documents/projects/scripts-and-snippets/
    $HOME/Documents/projects/wiki/
    $HOME/Documents/projects/work/schur-functions/
    $HOME/Documents/projects/work/gauge-integrability/
    $HOME/Documents/projects/work/spectral-curves/
    $HOME/Documents/projects/work/pySymmetricPolynomials
)

for repo in "${gitRepos[@]}"
do
    test -n "$(git -C $repo status --porcelain)" && echo ">> MODIFIED :: $repo" #|| echo "<< NOTHING :: $repo"
done

   

