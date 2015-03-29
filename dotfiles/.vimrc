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
NeoBundle 'kien/ctrlp.vim' "Ctr+P to search for files
NeoBundle 'rking/ag.vim'
NeoBundle 'tpope/vim-commentary' "to see help, ':h commentary
NeoBundle 'xolox/vim-misc' "to manage session
NeoBundle 'xolox/vim-session' "to manage session
NeoBundle 'Raimondi/delimitMate' "Closing autocompletion

call neobundle#end()



" Required:
filetype plugin indent on

" If there are uninstalled bundles found on
"startup,
" this will conveniently prompt you to
"install them.
NeoBundleCheck

" ColorScheme :
set  t_Co=256
" colorscheme github
" colorscheme desert

" display line number
set nu

" shortcut for NERDTree
let mapleader = ","
nmap <leader>ne :NERDTree<cr>

" Setting for good Python vizualization :
syntax on
set list listchars=tab:▷⋅,trail:⋅,nbsp:⋅
set statusline=%F%m%r%h%w\ [TYPE=%Y\ %{&ff}]\
			\ [%l/%L\ (%p%%)
filetype plugin indent on
au FileType py set autoindent
au FileType py set smartindent
au FileType py set textwidth=79 " PEP-8 Friendly

