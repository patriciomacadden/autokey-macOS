if window.get_active_class() == "konsole.konsole":
  keyboard.send_keys("<ctrl>+<shift>+c")
else:
  keyboard.send_keys("<ctrl>+c")