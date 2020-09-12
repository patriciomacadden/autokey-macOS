if window.get_active_class() == "konsole.konsole":
  keyboard.send_keys("<ctrl>+<shift>+v")
else:
  keyboard.send_keys("<ctrl>+v")
