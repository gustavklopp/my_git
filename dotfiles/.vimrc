 " Note: Skip initialization for vim-tiny or vim-small.
if !1 | finish | endif

if has('vim_starting')
	if &compatible
		set nocompatible               " Be iMproved
	endif
 
	" Required:
	set runtimepath+=~/.vim/bundle/neobundle.vim/
endif

" Required:
call neobundle#begin(expand('~/.vim/bundle/'))

" Let NeoBundle manage NeoBundle
" Required:
NeoBundleFetch 'Shougo/neobundle.vim'

" My Bundles here:
" Refer to |:NeoBundle-examples|.
" Note: You don't set neobundle setting in
 " .gvimrc!
NeoBundle 'scrooloose/nerdtree'
NeoBundle 'kien/ctrlp.vim'
NeoBundle 'rking/ag.vim'
NeoBundle 'tpope/vim-commentary'
NeoBundle 'xolox/vim-misc'
NeoBundle 'xolox/vim-session'

call neobundle#end()


" Required:
filetype plugin indent on

" If there are uninstalled bundles found on
"startup,
" this will conveniently prompt you to
"install them.
NeoBundleCheck


set  t_Co=256

"colorscheme github
colorscheme desert
set nu
"Open NERDTree automatically
"save session on quitting Vim
"autocmd VimLeave * NERDTreeClose

" Restore session on starting Vim

"autocmd VimEnter * NERDTree

" Remap NERDTree to ',ne' in normal  mode
let mapleader = ","
nmap <leader>ne :NERDTree<cr>
