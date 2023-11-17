<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link rel="stylesheet" href="/bootstrap.min.css" />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="test-center bg-primary text-white"
            style="border-top-right-radius: 10px; border-top-left-radius: 10px"
          >
            AI Club shopping list
          </h1>
          <hr />
          <br />

          <!-- Alert Message -->
          <b-alert variant="success" v-if="showMessage" show>{{
            message
          }}</b-alert>

          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal.product-modal
          >
            Add Product
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Link</th>
                <th scope="col">Quantity</th>
                <th scope="col">Bought?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in products" :key="index">
                <td>{{ product.name }}</td>
                <td>
                  <a :href="product.link">Amazon link for {{ product.name }}</a>
                </td>
                <td>{{ product.quantity }}</td>
                <td>
                  <span v-if="product.bought">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group">
                    <button
                      type="button"
                      class="btn btn-info btn-sm"
                      v-b-modal.product-update-modal
                      @click="editProduct(product)"
                    >
                      Update
                    </button>
                    <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      @click="deleteProduct(product)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="
              border-bottom-left-radius: 10px;
              border-bottom-right-radius: 10px;
            "
          >
            Made with ❤️ by iAV8.
          </footer>
        </div>
      </div>
      <!-- first Modal -->
      <b-modal
        ref="addProductModal"
        id="product-modal"
        title="Add a new Prdouct"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-name-group"
            label="Name:"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="addProductForm.name"
              required
              placeholder="Enter Name"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="form-link-group"
            label="Link:"
            label-for="form-link-input"
          >
            <b-form-input
              id="form-link-input"
              type="text"
              v-model="addProductForm.link"
              required
              placeholder="Enter Product Link"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-quantity-group"
            label="Quantity:"
            label-for="form-quantity-input"
          >
            <b-form-input
              id="form-quantity-input"
              type="number"
              v-model="addProductForm.quantity"
              required
              placeholder="Enter Quantity to buy"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-bought-group">
            <b-form-checkbox-group
              id="form-checks"
              v-model="addProductForm.bought"
            >
              <b-form-checkbox value="" true> Bought? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="outline-info">Add</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>

      <!-- for edit -->
      <b-modal
        ref="editProductModal"
        id="product-update-modal"
        title="Edit a Prdouct"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group
            id="form-name-group"
            label="Name:"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="editForm.name"
              required
              placeholder="Enter Name"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="form-link-group"
            label="Link:"
            label-for="form-link-input"
          >
            <b-form-input
              id="form-link-input"
              type="text"
              v-model="editForm.link"
              required
              placeholder="Enter Product Link"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-number-group"
            label="Number:"
            label-for="form-quantity-input"
          >
            <b-form-input
              id="form-quantity-input"
              type="number"
              v-model="editForm.quantity"
              required
              placeholder="Enter Quantity"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-bought-group">
            <b-form-checkbox-group id="form-checks" v-model="editForm.bought">
              <b-form-checkbox value="" true> Bought? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="outline-info">Update</b-button>
          <b-button type="reset" variant="outline-danger">Cancel</b-button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      products: [],
      addProductForm: {
        name: "",
        link: "",
        quantity: 0,
        bought: [],
      },
      editForm: {
        id: "",
        name: "",
        quantity: 0,
        link: "",
        bought: "",
      },
    };
  },

  methods: {
    //get function
    getProducts() {
      const path = "http://127.0.0.1:5000/products";
      axios
        .get(path)
        .then((res) => {
          this.products = res.data.products;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    //post function
    addProduct(payload) {
      const path = "http://127.0.0.1:5000/products";
      axios
        .post(path, payload)
        .then((res) => {
          this.getProducts();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getProducts();
        });
    },
    initForm() {
      this.addProductForm.name = "";
      this.addProductForm.link = "";
      this.addProductForm.quantity = 0;
      this.addProductForm.bought = [];
      this.editForm.id = "";
      this.editForm.name = "";
      this.editForm.link = "";
      this.editForm.quantity = 0;
      this.editForm.bought = [];
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addProductModal.hide();
      let bought = false;
      if (this.addProductForm.bought[0]) bought = true;
      const payload = {
        name: this.addProductForm.name,
        link: this.addProductForm.link,
        quantity: this.addProductForm.quantity,
        bought,
      };
      this.addProduct(payload);
      this.initForm();
    },

    onReset(e) {
      e.preventDefault();
      this.$ref.addProductModal.hide();
      this.initForm();
    },

    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.editProductModal.hide();
      let bought = false;
      if (this.editForm.bought[0]) bought = true;
      const payload = {
        name: this.editForm.name,
        link: this.editForm.link,
        quantity: this.editForm.quantity,
        bought,
      };
      this.updateProduct(payload, this.editForm.id);
    },

    onResetUpdate(e) {
      e.preventDefault();
      this.$refs.addProductModal.hide();
      this.initForm();
      this.getProducts();
    },

    updateProduct(payload, productID) {
      const path = `http://127.0.0.1:5000/products/${productID}`;
      axios
        .put(path, payload)
        .then((res) => {
          this.getProducts();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getProducts();
        });
    },

    removeProduct(productID) {
      const path = `http://127.0.0.1:5000/products/${productID}`;
      axios
        .delete(path)
        .then((res) => {
          this.getProducts();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getProducts();
        });
    },
    editProduct(product) {
      this.editForm = product;
    },
    deleteProduct(product) {
      this.removeProduct(product.id);
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
