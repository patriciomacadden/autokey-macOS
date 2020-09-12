if window.get_active_class() == "konsole.konsole":
  keyboard.send_keys("<ctrl>+<shift>+t")
else:
  keyboard.send_keys("<ctrl>+t")
