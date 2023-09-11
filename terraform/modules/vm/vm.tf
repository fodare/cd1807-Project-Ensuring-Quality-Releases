resource "azurerm_virtual_network" "test-vn" {
  name                = "example-vn"
  address_space       = ["10.5.0.0/16"]
  location            = var.location
  resource_group_name = var.resource_group_name
}

resource "azurerm_subnet" "test-subn" {
  name                 = "internal-subnet"
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.test-vn.name
  address_prefixes     = ["10.5.1.0/24"]
}

resource "azurerm_network_interface" "test-ni" {
  name                = "example-nic"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.test-subn.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "test-ni" {
  name                  = "test-vm"
  location              = var.location
  resource_group_name   = var.resource_group_name
  size                  = "Standard_DS2_v2"
  admin_username        = var.admin_username
  network_interface_ids = [azurerm_network_interface.test-ni.id, azurerm_subnet.test-subn.id]
  admin_ssh_key {
    username   = "adminUser"
    public_key = file("~/.ssh/azure_rsa.pub")
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
