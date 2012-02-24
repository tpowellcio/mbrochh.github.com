Date: 2012-02-29
Title: Snippets February 2012
Slug: snippets-201202
Category: Blog
Tags: git, python
status: draft

# What is this about?

# Global .gitignore_global

    ::text
    [core]
    editor = nano
    excludesfile = $HOME/.gitignore_global

# Better Omni Completion in vim

    ::text
    set completeopt=longest,menuone

    " found here: http://stackoverflow.com/a/2170800/70778
    function! OmniPopup(action)
        if pumvisible()
            if a:action == 'j'
                return "\<C-N>"
            elseif a:action == 'k'
                return "\<C-P>"
            endif
        endif
        return a:action
    endfunction
    inoremap <silent><C-j> <C-R>=OmniPopup('j')<CR>
    inoremap <silent><C-k> <C-R>=OmniPopup('k')<CR>

# Showing git branch in prompt

    ::sh
    brew install git

    ::text
    export PS1='\w\[\033[31m\]$(__git_ps1 "(%s)") \[\033[01;34m\]$\[\033[00m\] '
