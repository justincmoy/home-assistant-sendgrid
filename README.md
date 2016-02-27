# home-assistant-sendgrid
The SendGrid Home Assistant notification component allows you to send notifications from Home Assistant to an email recipient via SendGrid.
[Home Assistant](https://home-assistant.io) is an open source home automation platform.
[SendGrid](https://sendgrid.com/) is a proven cloud-based email platform.

This was accepted upstream and will be included in the 0.14 release of Home Assistant: https://github.com/balloob/home-assistant/pull/1419

# Installation
Place sendgrid.py in `<config directory>/custom_components/`.
For more information, check out [Home Assistant's custom components](https://home-assistant.io/developers/creating_components/#loading-components).

# Configuration
To enable notification by email in your installation, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
notify:
  name: NOTIFIER_NAME
  platform: sendgrid
  api_key: API_KEY
  sender: SENDER_EMAIL_ADDRESS
  recipient: YOUR_RECIPIENT
```

Configuration variables:

- **name** (*Optional*): Setting the optional parameter `name` allows multiple notifiers to be created. The default value is `notify`. The notifier will bind to the service `notify.NOTIFIER_NAME`.
- **api_key** (*Required*): SendGrid API key - https://app.sendgrid.com/settings/api_keys
- **sender** (*Required*): E-mail address of the sender.
- **recipient** (*Required*): Recipient of the notification.
