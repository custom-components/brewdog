# custom_component to get info about a random beer

A platform which allows you to get information about a random BrewDog beer.
  
To get started put `/custom_components/brewdog/sensor.py` here:  
`<config directory>/custom_components/brewdog/sensor.py`  
  
**Example configuration.yaml:**

```yaml
sensor:
  platform: brewdog
```

**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The platform name.  
  
## Sample overview

![Sample overview](overview.png)
  
***

Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.

***

[![BuyMeCoffee](https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667)](https://www.buymeacoffee.com/ludeeus)
