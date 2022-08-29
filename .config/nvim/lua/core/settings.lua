--
-- Neovim Core Settings
--

-- UI
vim.o.termguicolors             = true
vim.o.scrolloff                 = 8
vim.o.number                    = true
vim.o.cursorline                = true

-- Windows | Tabs | Buffers
vim.o.splitright                = true
vim.o.splitbelow                = true

-- Editing
vim.o.expandtab                 = true
vim.o.tabstop                   = 2
vim.o.shiftwidth                = 2
vim.o.cindent                   = true
vim.o.wrap                      = false

-- Functionality
vim.o.clipboard                 = 'unnamedplus'

-- Search
vim.o.ignorecase                = true
vim.o.smartcase                 = true

-- Backups / Undos
vim.o.backup                    = false
vim.o.writebackup               = false
vim.o.swapfile                  = false
vim.o.undofile                  = true

