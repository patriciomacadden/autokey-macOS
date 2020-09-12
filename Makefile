install:
	mkdir -p $$HOME/.config/autokey/data/macOS
	stow -t $$HOME/.config/autokey/data/macOS -R .

uninstall:
	stow -t $$HOME/.config/autokey/data/macOS -D .
	rmdir $$HOME/.config/autokey/data/macOS